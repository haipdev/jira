import logging
import os
import pytest
import haip.config as config
import haip.jira as jira

logging.basicConfig()
logger = logging.getLogger('haip')
logger.setLevel(logging.DEBUG)

@pytest.fixture
def setup():
    basedir = os.path.dirname(__file__)
    config.load(basedir + os.sep + 'etc', 'dev')

@pytest.mark.skip(reason="you need a running jira server for this test")
@pytest.mark.asyncio
async def test_get(setup):
    response = await jira.get('PROBLEM-53531')
    print(response)
    assert True == True
    
