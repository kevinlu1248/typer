import pytest
import typer
from pydantic import EmailStr, HttpUrl

def test_email_str():
    app = typer.Typer()

    @app.command()
    def main(email: EmailStr):
        return email

    runner = typer.Tester(app)
    result = runner.invoke(["main", "not_an_email"])
    assert result.exit_code != 0, "Invalid email should not pass validation"

    result = runner.invoke(["main", "test@example.com"])
    assert result.exit_code == 0, "Valid email should pass validation"

def test_http_url():
    app = typer.Typer()

    @app.command()
    def main(url: HttpUrl):
        return url

    runner = typer.Tester(app)
    result = runner.invoke(["main", "not_a_url"])
    assert result.exit_code != 0, "Invalid URL should not pass validation"

    result = runner.invoke(["main", "http://example.com"])
    assert result.exit_code == 0, "Valid URL should pass validation"