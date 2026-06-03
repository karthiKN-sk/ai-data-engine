from models.model_type import ModelType

class LLMRouter:

    def generate_report(
        self,
        model: ModelType,
        validation_report: dict,
        quality_report: dict,
        transformation_report: dict,
    ) -> str:
        
        print(f"\nUSING MODEL: {model.value}\n")
        
        prompt = self.build_prompt(
            validation_report,
            quality_report,
            transformation_report,
        )

        print("\nPROMPT SENT TO MODEL\n")
        print(prompt)

        return f"""
        AI GENERATED REPORT

        Quality Score: {quality_report['quality_score']}%

        Errors Found:
        {validation_report['error_count']}

        Average Salary:
        {transformation_report['average_salary']}

        Top Departments:
        {transformation_report['department_counts']}

        Recommendations:
        - Fix invalid age values
        - Fix invalid emails
        - Complete missing salaries
        """
    

    def build_prompt(
        self,
        validation_report,
        quality_report,
        transformation_report,
    ) -> str:

        return f"""
        You are a Senior Data Engineering Analyst.

        Validation Report:
        {validation_report}

        Quality Report:
        {quality_report}

        Transformation Report:
        {transformation_report}

        Generate:
        1. Executive Summary
        2. Data Quality Assessment
        3. Insights
        4. Recommendations
        """