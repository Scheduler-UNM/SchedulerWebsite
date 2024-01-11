# Django Project Backend Documentation

## Overview

This Django project comprises two main applications: `common` and `employee`.

## Apps Description

### Common App
The `common` app includes models and functionalities related to the general operations of the system.

- **Models**:
  - `Terms`
  - `Pods`
  - `Shifts`
  - `ShiftRequest`
- **Views**:
  - Contains functions to add objects for each model mentioned above, located in `views.py`.
  - Most of the function are added in the `views.py` file. 
- **HTML Templates**:
  - HTML files for testing are located in `templates/common/` & `templates/employee/`. These are initial drafts and might require further development.
  - HTML files should be in their respective `templates/app_name/` folder. 

### Employee App
The `employee` app handles functionalities related to employees and their access management.

- **Models**:
  - `Employee`
  - `Access`
- **Views**:
  - Includes a function to add `Employee` objects, defined in `views.py`.
- **HTML Templates**:
  - Test HTML files are in `templates/employee/`. These may need to be updated or rewritten.

## Template Structure

- HTML templates are stored in the respective `template/app_name` directories for each app.
- If separate folders are created for templates, ensure to update the `TEMPLATES` configuration in `settings.py`.

## Database Configuration

- The project uses SQLite, Django's default database.
- Integration with other database systems is possible. Any change in the database configuration must be reflected in the `settings.py` file.

## URL Routing

- **Project’s `urls.py`**: Routes to the appropriate app’s `urls.py`.
- **App’s `urls.py`**: Defines the specific pages that are rendered for each URL.

## Integration Notes

- Functions in `views.py` need adjustments to ensure proper backend integration.
- The current HTML templates are for initial testing and likely need further modifications.



