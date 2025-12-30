# API Reference

Documentation for internal data APIs.

## Data Pipeline API

### PipelineRunner

```python
class PipelineRunner:
    """
    Main class for running data pipelines.
    
    Attributes:
        config (PipelineConfig): Pipeline configuration
        logger (Logger): Pipeline logger
    """
    
    def __init__(self, config: PipelineConfig):
        """
        Initialize the pipeline runner.
        
        Args:
            config: Pipeline configuration object
        """
        self.config = config
        self.logger = self._setup_logger()
    
    def run(self, dry_run: bool = False) -> PipelineResult:
        """
        Execute the pipeline.
        
        Args:
            dry_run: If True, validate without executing
            
        Returns:
            PipelineResult with execution details
            
        Raises:
            PipelineError: If pipeline execution fails
        """
        pass
    
    def validate(self) -> ValidationResult:
        """
        Validate pipeline configuration and dependencies.
        
        Returns:
            ValidationResult with any issues found
        """
        pass
```

### DataValidator

| Method | Description | Returns |
|--------|-------------|---------|
| `check_nulls(df, columns)` | Check for null values | `ValidationResult` |
| `check_duplicates(df, keys)` | Check for duplicate keys | `ValidationResult` |
| `check_schema(df, schema)` | Validate against schema | `ValidationResult` |
| `check_range(df, column, min, max)` | Check value ranges | `ValidationResult` |

## Usage Example

```python
from pipeline import PipelineRunner, PipelineConfig

# Configure and run
config = PipelineConfig(
    name="daily_sales",
    source="postgresql://...",
    target="s3://data-lake/sales/"
)

runner = PipelineRunner(config)

# Validate first
validation = runner.validate()
if validation.is_valid:
    result = runner.run()
    print(f"Pipeline completed: {result.rows_processed} rows")
```
