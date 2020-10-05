import os
import tempfile

import pytest
from app import create_app
from app import db


@pytest.fixture(scope="function")
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()

    with flask_app.app_context():
        db_file_directory, db_file = tempfile.mkstemp()
        flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_file
        flask_app.config["TESTING"] = True

        db.create_all()

        yield testing_client

        os.close(db_file_directory)
