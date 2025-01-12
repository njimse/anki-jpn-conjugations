"""Miscellaneous utilities that don't otherwise have a good home"""
import re

def remove_furigana(reading: str) -> str:
    """Remove the furigana markup from a reading text
    
    Parameters
    ----------
    reading : str
        Input string which potentially contains furigana markup
    
    Returns
    -------
    str
        Input string with all furigana markup removed
    """
    # import pdb; pdb.set_trace()
    return re.sub(r"(^| )(\S+)(\[[^\]]+\])", r"\2", reading, flags=re.UNICODE)

def promote_furigana(reading: str) -> str:
    """Promote furigana markup such that it replaces the associated text
    
    Parameters
    ----------
    reading : str
        Input string which potentially contains furigana markup
    
    Returns
    -------
    str
        Input string modified such that furigana markup is used to replace
        any corresponding text
    """

    return re.sub(r"(^| )(\S+)\[([^\]]+)\]", r"\3", reading, flags=re.UNICODE)