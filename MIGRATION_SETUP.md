# Alembic Migration Setup

After setting up the project, run the following commands to create and apply the initial migration:

```bash
# Create the initial migration
alembic revision --autogenerate -m "init"

# Apply the migration
alembic upgrade head
```

The migration will create the `users` and `sensors` tables in the PostgreSQL database.

