CREATE TABLE public.best_number
(
    "number" integer,
    created timestamp with time zone
)

TABLESPACE pg_default;

ALTER TABLE public.best_number
    OWNER to postgres;