# Deployment Guide

How to deploy pipelines to production.

## Deployment Flow

```{mermaid}
flowchart LR
    A[Local Dev] --> B[PR Review]
    B --> C[Staging]
    C --> D[QA Tests]
    D --> E{Pass?}
    E -->|Yes| F[Production]
    E -->|No| A
    
    style F fill:#c8e6c9
```

## Pre-Deployment Checklist

- [ ] All tests passing
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] Rollback plan documented
- [ ] Monitoring alerts configured

## Deployment Steps

### 1. Create Release Branch

```bash
git checkout main
git pull origin main
git checkout -b release/v1.2.0
```

### 2. Run Integration Tests

```bash
pytest tests/integration/ -v
```

### 3. Deploy to Staging

```bash
# Deploy using CI/CD
git push origin release/v1.2.0

# Or manual deploy
./scripts/deploy.sh staging
```

### 4. Validate in Staging

```sql
-- Verify data quality
SELECT COUNT(*) FROM staging.processed_data
WHERE processing_date = CURRENT_DATE;
```

### 5. Deploy to Production

```bash
# Merge to main triggers production deploy
git checkout main
git merge release/v1.2.0
git push origin main
```

```{warning}
Always deploy to staging first and validate before production deployment.
```

## Rollback Procedure

If issues are detected:

```bash
# Revert to previous version
git revert HEAD
git push origin main

# Restore data if needed
./scripts/restore_backup.sh production
```
