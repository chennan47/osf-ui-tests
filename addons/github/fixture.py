from pages import FILES
from pages.helpers import create_user
from tests.fixtures import ProjectFixture, SubprojectFixture


class GithubaddonFixture(ProjectFixture):
    @classmethod
    def setUpClass(cls):
        super(GithubaddonFixture, cls).setUpClass()

        _url = cls.page.driver.current_url
        cls.page.settings.addon_selection("GitHub")
        cls.page.settings.get_token("github")
        cls.page.settings.set_repo("github", ['osftest', 'addontesting'])
        cls.page.driver.get(_url)



