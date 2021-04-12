from sys import stdout
from loguru import logger

log_format = [
    '{time: YYYY-MM-DD hh:mm:ss}',
    '{file: <15}',
    '{function: <15}',
    '{line: 03d}',
    '<R>{level: ^10}</R>',
    '{message}'
]
logger.remove()
logger.add(
    sink=stdout,
    level='TRACE',
    format=' | '.join(log_format)
)