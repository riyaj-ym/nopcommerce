import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(
            filename="L:/nopcommerce/Logs/automation.log",
            force=True,
            format="%(asctime)s: %(levelname)s: %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p",
            filemode="w",
        )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
