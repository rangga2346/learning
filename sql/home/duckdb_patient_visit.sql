SELECT

    CAST("Visit Date" AS DATE)                 AS "Visit Date",
    Month,
    Hospital,
    Department,
    Doctor,
    "Patient Type",
    Gender,
    "Visit Type",

    CAST("Patient Count" AS INTEGER)          AS "Patient Count",

    CAST(Revenue AS DOUBLE)                   AS Revenue,

    CAST("Target Revenue" AS DOUBLE)          AS "Target Revenue",

    CAST("Patient Age" AS INTEGER)            AS "Patient Age",

    CAST("Waiting Time" AS INTEGER)           AS "Waiting Time",

    CAST("Length of Stay" AS INTEGER)         AS "Length of Stay",

    CAST( REPLACE("Target Achievement (%)", ',', '.') AS DOUBLE) AS "Target Achievement (%)",
    CAST( REPLACE("Latitude", ',', '.') AS DOUBLE) AS "Latitude",
    CAST( REPLACE("Longitude", ',', '.') AS DOUBLE) AS "Longitude"


FROM patient_visit_dummy;