from abc import ABC, abstractmethod
from typing import Any, List
import re


class PipelineStep(ABC):
    """ An abstract base class representing a single step in a processing pipeline. """
    @abstractmethod
    def process(self, data: Any) -> Any:
        """ Processes the input data and returns the result.
        This method must be implemented by all concrete subclasses. """
        pass
    
    
class DataLoader(PipelineStep):
    """ Loads data from a text file, returning a list of lines. """
    def process(self, filepath: str) -> List[str]:
        try:
            with open(filepath, "r", encoding="utf-8") as f: # utf-8 is for universal charchters usage 
                breakpoint()
                return f.read().splitlines()
            
        except FileNotFoundError:
            return []
        
            
class Preprocessor(PipelineStep):
    """ Cleans a list of text strings by converting to lowercase, removing punctuation, and stripping extra whitespace. """
    def __init__(self, punctuation_to_remove: str = r'[^\w\s]'):
        self.punctuation_pattern = re.compile(punctuation_to_remove)
        
        
    def process(self, data: List[str]) -> List[str]:
        return [re.sub(self.punctuation_pattern, "", text.lower().strip()) for text in data ]
    
    
class Analyzer(PipelineStep):
    """ Analyzes the text data to compute basic statistics. """
    def process(self, data: List[str]) -> dict:
        """ Calculates total lines, average words per line, and number of unique words. """

        total_lines = 0
        total_words = 0
        unique_words = set()
        
        for line in data:
            total_lines += 1 # Count empty lines too. To count only non-empty lines move this line after if condition.
            if not line:
                continue 
            for word in line.split():
                total_words += 1
                unique_words.add(word)

        avg_length = total_words / total_lines if total_lines else 0 
        return {"total_lines": total_lines,
                "avg_length": avg_length,
                "unique_words": len(unique_words)
                }


class ReportGenerator:
    """ Generates and outputs reports from the analysis statistics. """
    def print_to_console(self, stats: dict):
        """ Prints the statistics in a formatted way to the console. """
        for key, value in stats.items():
            statics = key.replace("_", " ").title()
            print(f"{statics}: {value}")
        
    
    def save_to_file(self, stats: dict, filepath: str):
        """ Saves the statistics in a formatted way to a text file. """
        try:
            lines = []
            for key, value in stats.items():
                statics = key.replace("_", " ").title()
                lines.append(f"{statics}: {value}\n")
            with open(filepath, "w", encoding="utf-8") as f: # utf-8 is for universal charchters usage 
                return f.writelines(lines)
        except FileNotFoundError:
            return []


class AIPipeline:
    """ Orchestrates a series of pipeline steps to process data. """
    def __init__(self, *steps: PipelineStep):
        self.steps = steps
        
    def run(self, initial_input: Any) -> Any:
        """ Executes all steps in the pipeline sequentially. """
        # result = initial_input
        for step in self.steps:
            initial_input = step.process(initial_input)
        return initial_input
        
