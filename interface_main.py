class IParser:
    def load_data_source(self, path: str, file_name:str) -> str:
        """ Load in the file for extracting text.
            It defines the two methods .load_data_source() and .extract_text()
            These methods are defined but not implemented. 
            The implementation will occur once you create concrete classes that inherit from IParser
        """
        pass
    
    def extract_text(self, full_file_name: str) -> str:
        """Extract text from the currently loaded file."""
        pass
    

class PdfParser(IParser):
    """Extract text from a PDF"""
    def load_data_source(self, path:str, file_name: str) -> str:
        """Overrides IParser.load_data_source()"""
        pass
    
    def extract_text(self, full_file_path: str) -> dict:
        """Overrides IParser.extract_text()"""
        pass
    
    
class EmailParser(IParser):
    """Extract text from an email"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides IParser.load_data_source()"""
        pass
    
    def extract_text_from_email(self, full_file_path: str) -> str:
        """A method defined only in EmailParser.
        Does not override IParser.extract_text() 
        """
        pass
        

