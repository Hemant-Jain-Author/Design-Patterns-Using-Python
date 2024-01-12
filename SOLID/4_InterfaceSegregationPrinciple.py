from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self):
        pass

class Faxable(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class BasicInkjetPrinter(Printable, Scannable):
    def print(self, document):
        print(f"Printing {document} using basic inkjet printer")

    def scan(self):
        print("Scanning using basic inkjet printer")

class HighEndOfficePrinter(Printable, Scannable, Faxable):
    def print(self, document):
        print(f"Printing {document} using high end office printer")

    def scan(self):
        print("Scanning using high end office printer")

    def fax(self, document):
        print(f"Faxing {document} using high end office printer")

# Client code
basic_printer = BasicInkjetPrinter()
basic_printer.print("Sample Document")
basic_printer.scan()

office_printer = HighEndOfficePrinter()
office_printer.print("Important Report")
office_printer.scan()
office_printer.fax("Confidential Memo")

"""
Printing Sample Document using basic inkjet printer
Scanning using basic inkjet printer
Printing Important Report using high end office printer
Scanning using high end office printer
Faxing Confidential Memo using high end office printer
"""