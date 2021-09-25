import re


class HelperValidation:
    """
    Contains helper validation methods which commonly will be
    used for entire project
    """
    @staticmethod
    def is_valid_name(name):
        """
        returns true if the name is valid
        """
        reg = r'^[a-zA-Z. ]{0,150}$'
        return True if re.search(reg, name) else False
