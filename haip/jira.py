import logging
import aiohttp 
import haip.config as config

_logger = logging.getLogger(__name__)

def getSession():
    cfg = config.get('jira', username=None, password=None, timeout=10)
    params = {'timeout': aiohttp.ClientTimeout(total=cfg.timeout)}
    if cfg.username is not None:
        params['auth'] = aiohttp.BasicAuth(cfg.username, cfg.password)
    return aiohttp.ClientSession(**params)

async def get(key):
    cfg = config.get('jira', url=config.MANDATORY)
    url = cfg.url + '/' + 'issue' + '/' + key
    async with getSession() as session:
        async with session.get(url, headers={'Content-Type': 'application/json'}) as response:
            return await response.json()


