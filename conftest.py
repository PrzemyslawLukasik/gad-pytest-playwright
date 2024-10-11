from pathlib import Path

import pytest

from src.helpers.screenshots import Screenshots


def pytest_addoption(parser):
    """
    Custom input parameters
    """
    parser.addoption(
        "--base_url",
        action="store",
        dest="base_url",
        default="http://localhost:3000",
        help="Default part of the url of the application",
    )
    parser.addoption(
        "--screenshot-path",
        action="store",
        dest="screenshot_path",
        default="artefacts/screenshots",
        help="Path to the screenshots folder",
    )
    parser.addoption(
        "--additional-info",
        action="store",
        dest="additional_info",
        default="Build: ",
        help="Path to the screenshots folder",
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Create report with the screenshoot if the UI mark was used
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screenshot_path = ""
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)
    extras = getattr(report, "extras", [])
    if report.when == "call" and "page" in item.funcargs:
        if report.failed and "page" in item.funcargs:
            page = item.funcargs["page"]
            # tracing_path = item.config.option.tracing_path + "/" + item.name + ".zip"
            # page.context.tracing.stop(path=tracing_path)
            screenshot_path = item.config.option.screenshot_path
            if screenshot_path:
                screenshots = Screenshots(
                    relative_path=Path(screenshot_path), page=page
                )
                screenshots.save_screenshot_as_file(item.name)
            screenshot_base64 = Screenshots(
                relative_path=Path(""), page=page
            ).save_screenshot_as_base64()
            extras.append(pytest_html.extras.image(screenshot_base64))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # add the screenshots to the html report
            page = item.funcargs["page"]
            screenshot_base64 = Screenshots(
                relative_path=Path(""), page=page
            ).save_screenshot_as_base64()
            extras.append(pytest_html.extras.image(screenshot_base64))
        report.extras = extras
