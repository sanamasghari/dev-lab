from pipeline import (
    DataLoader,
    Preprocessor,
    Analyzer,
    ReportGenerator,
    AIPipeline
    )
import os

if __name__ == "__main__":
    # --- Component Definitions ---
    loader = DataLoader()
    preprocessor = Preprocessor()
    basic_analyzer = Analyzer()
    reporter = ReportGenerator()
    input_filepath = "/home/sanam/Desktop/ai_daneshkar_bootcamp/python/assignment/2/ai_pipeline_project/src/pipeline_project/sample_data.txt"
    
    # --- Pipeline ---
    print("\n--- Running Pipeline ---")
    basic_pipeline = AIPipeline(loader, preprocessor, basic_analyzer)
    basic_results = basic_pipeline.run(input_filepath)
    reporter.print_to_console(basic_results)
