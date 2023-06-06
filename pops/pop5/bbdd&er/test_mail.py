import sqlite3
from pathlib import Path
from types import GeneratorType

import create_db
import pytest
from mail import DbUtils, Mail, MailError, MailServer

TEST_DB_PATH = "test_mail.db"

# **************************************************************
# FIXTURES
# **************************************************************


@pytest.fixture(autouse=True)
def create_test_database():
    create_db.create(TEST_DB_PATH)
    yield
    Path(TEST_DB_PATH).unlink(missing_ok=True)


@pytest.fixture(autouse=True)
def make_dbutils_use_test_database(monkeypatch: pytest.MonkeyPatch):
    sconnect = sqlite3.connect

    def mock_sqlite3_connect(*args, **kwargs):
        return sconnect(TEST_DB_PATH)

    monkeypatch.setattr(sqlite3, "connect", mock_sqlite3_connect)


@pytest.fixture
def mailserver1():
    return MailServer("anna", "python")


@pytest.fixture
def mailserver2():
    return MailServer("evva", "rust")


@pytest.fixture
def mailserver3():
    return MailServer("anna", "fython")


@pytest.fixture
def mailserver4():
    return MailServer("evva", "yust")


@pytest.fixture
def mail1():
    return Mail(
        sender="vanrossum@python.org",
        recipient="galindo@python.org",
        subject="Hi there",
        body="Are you ok?",
    )


@pytest.fixture
def db_con():
    con = sqlite3.connect(TEST_DB_PATH)
    con.row_factory = sqlite3.Row
    yield con
    con.close()


# **************************************************************
# TESTS
# **************************************************************


def test_build_dbutils():
    d = DbUtils()
    assert isinstance(d.con, sqlite3.Connection)
    assert d.con.row_factory == sqlite3.Row
    assert isinstance(d.cur, sqlite3.Cursor)


def test_build_mail(mail1: Mail):
    assert isinstance(mail1, Mail)
    assert mail1.sender == "vanrossum@python.org"
    assert mail1.recipient == "galindo@python.org"
    assert mail1.subject == "Hi there"
    assert mail1.body == "Are you ok?"

    assert isinstance(mail1.con, sqlite3.Connection)
    assert isinstance(mail1.cur, sqlite3.Cursor)


def test_mail_class_inherits_dbutils():
    assert issubclass(Mail, DbUtils)


def test_send_mail(mail1: Mail, db_con: sqlite3.Connection):
    mail1.send()
    sql = 'SELECT * FROM activity WHERE sender="vanrossum@python.org"'
    result = db_con.cursor().execute(sql)
    row = result.fetchall()
    assert len(row) == 1
    assert row[0]["sender"] == "vanrossum@python.org"
    assert row[0]["recipient"] == "galindo@python.org"
    assert row[0]["subject"] == "Hi there"
    assert row[0]["body"] == "Are you ok?"


def test_mail_representation_as_string(mail1: Mail):
    assert (
        str(mail1)
        == """From: vanrossum@python.org
To: galindo@python.org
---
HI THERE:
Are you ok?"""
    )


def test_build_mailserver(mailserver1: MailServer):
    assert isinstance(mailserver1, MailServer)
    assert mailserver1.username == "anna"
    assert mailserver1.password == "python"
    assert mailserver1.logged is False

    assert isinstance(mailserver1.con, sqlite3.Connection)
    assert isinstance(mailserver1.cur, sqlite3.Cursor)


def test_mailserver_class_inherits_dbutils():
    assert issubclass(MailServer, DbUtils)


def test_mailserver_login(mailserver1: MailServer, mailserver2: MailServer):
    mailserver1.login()
    assert mailserver1.logged is True
    assert mailserver1.domain == "gmail.com"

    mailserver2.login()
    assert mailserver2.logged is True
    assert mailserver2.domain == "icloud.com"


def test_mailserver_login_fails_when_password_is_wrong(
    mailserver3: MailServer, mailserver4: MailServer
):
    mailserver3.login()
    assert mailserver3.logged is False
    assert mailserver3.domain == ""

    mailserver4.login()
    assert mailserver4.logged is False
    assert mailserver4.domain == ""


def test_sender_representation(mailserver1: MailServer, mailserver2: MailServer):
    with pytest.raises(AttributeError):
        assert mailserver1.sender == "anna@gmail.com"
        assert mailserver2.sender == "evva@icloud.com"
    mailserver1.login()
    assert mailserver1.sender == "anna@gmail.com"
    mailserver2.login()
    assert mailserver2.sender == "evva@icloud.com"


def test_send_mail_from_mailserver(mailserver1: MailServer, db_con: sqlite3.Connection):
    RECIPIENT = "stinner@python.org"
    SUBJECT = "New Python"
    BODY = "We are launching a new Python version!"

    mailserver1.login()
    mailserver1.send_mail(
        recipient=RECIPIENT,
        subject=SUBJECT,
        body=BODY,
    )
    sql = "SELECT * FROM activity WHERE recipient=?"
    result = db_con.cursor().execute(sql, (RECIPIENT,))
    rows = result.fetchall()
    assert len(rows) == 1
    assert rows[0]["sender"] == "anna@gmail.com"
    assert rows[0]["recipient"] == RECIPIENT
    assert rows[0]["subject"] == SUBJECT
    assert rows[0]["body"] == BODY


def test_send_mail_from_mailserver_fails_when_not_logged_in(mailserver1: MailServer):
    RECIPIENT = "stinner@python.org"
    SUBJECT = "New Python"
    BODY = "We are launching a new Python version!"

    with pytest.raises(MailError) as err:
        mailserver1.send_mail(
            recipient=RECIPIENT,
            subject=SUBJECT,
            body=BODY,
        )
    assert str(err.value) == 'User "anna" not logged in!'


def test_send_mail_from_mailserver_fails_when_invalid_recipient_email_format(
    mailserver1: MailServer,
):
    RECIPIENTS = ("stinner$python.org", "stinner@python", "stinner@python&org")
    SUBJECT = "New Python"
    BODY = "We are launching a new Python version!"

    mailserver1.login()
    for recipient in RECIPIENTS:
        with pytest.raises(MailError) as err:
            mailserver1.send_mail(
                recipient=recipient,
                subject=SUBJECT,
                body=BODY,
            )
        assert str(err.value) == f'Recipient "{recipient}" has invalid mail format!'


def test_get_sent_emails_from_mailserver(
    mailserver1: MailServer, db_con: sqlite3.Connection
):
    EMAILS = (
        ("anna@gmail.com", "core1@python.org", "Subject1", "Body1"),
        ("anna@gmail.com", "core2@python.org", "Subject2", "Body2"),
        ("anna@gmail.com", "core3@python.org", "Subject3", "Body3"),
        ("anna@gmail.com", "core4@python.org", "Subject4", "Body4"),
    )
    sql = "INSERT INTO activity(sender, recipient, subject, body) VALUES (?, ?, ?, ?)"
    db_cur = db_con.cursor()
    db_cur.executemany(sql, EMAILS)
    db_con.commit()

    mailserver1.login()
    emails = mailserver1.get_emails(sent=False)
    assert isinstance(emails, GeneratorType)
    for email, expected_email in zip(emails, EMAILS):
        sender, recipient, subject, body = expected_email
        assert email.sender == sender
        assert email.recipient == recipient
        assert email.subject == subject
        assert email.body == body


def test_get_received_emails_from_mailserver(
    mailserver1: MailServer, db_con: sqlite3.Connection
):
    EMAILS = (
        ("core1@python.org", "anna@gmail.com", "Subject1", "Body1"),
        ("core2@python.org", "anna@gmail.com", "Subject2", "Body2"),
        ("core3@python.org", "anna@gmail.com", "Subject3", "Body3"),
        ("core4@python.org", "anna@gmail.com", "Subject4", "Body4"),
    )
    sql = "INSERT INTO activity(sender, recipient, subject, body) VALUES (?, ?, ?, ?)"
    db_cur = db_con.cursor()
    db_cur.executemany(sql, EMAILS)
    db_con.commit()

    mailserver1.login()
    emails = mailserver1.get_emails(sent=False)
    assert isinstance(emails, GeneratorType)
    for email, expected_email in zip(emails, EMAILS):
        sender, recipient, subject, body = expected_email
        assert email.sender == sender
        assert email.recipient == recipient
        assert email.subject == subject
        assert email.body == body


def test_send_mail_from_mailserver_only_works_with_named_arguments(
    mailserver1: MailServer,
):
    mailserver1.login()
    with pytest.raises(TypeError):
        mailserver1.send_mail("rufus@gg.es", "It fails", "Good day!")


@pytest.mark.parametrize("mail_fixture", ("mail1", "mailserver1"))
def test_build_mail_error_and_close_connection(
    mail_fixture: str, request: pytest.FixtureRequest
):
    mail = request.getfixturevalue(mail_fixture)
    MailError("Houston we have a problem", mail)
    with pytest.raises(sqlite3.ProgrammingError) as db_err:
        mail.cur.execute("SELECT * FROM activity")
    assert str(db_err.value) == "Cannot operate on a closed database."


@pytest.mark.parametrize("mail_fixture", ("mail1", "mailserver1"))
def test_build_mail_error_and_repr(mail_fixture: str, request: pytest.FixtureRequest):
    mail = request.getfixturevalue(mail_fixture)
    err = MailError("Houston we have a problem", mail)
    assert str(err) == "Houston we have a problem"
