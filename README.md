# User Feedback API

## Overview

This project implements a REST API for collecting user feedback using Python Flask and SQLAlchemy. The API allows users to submit feedback via a POST request and stores the data in a PostgreSQL database.

## Features

- Accepts user feedback in JSON format.
- Validates input data.
- Stores validated feedback in a PostgreSQL database.

## Technologies Used

- **Python**: Programming language for the API.
- **Flask**: Micro web framework for building the API.
- **SQLAlchemy**: ORM for database interaction.
- **PostgreSQL**: Database for storing feedback.

## API Endpoint

### POST /feedback

#### Request Body

```json
{
    "FromId": 123,
    "Score": 2,
    "Description": "a text that could be everything",
    "UserPhoneNumber": "9647831234567"
}
