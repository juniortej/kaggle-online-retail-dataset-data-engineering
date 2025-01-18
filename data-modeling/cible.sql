CREATE TABLE "transactions" (
  "basket_id" varchar,
  "product_id" integer,
  "product_description" varchar,
  "quantity" float,
  "transaction_datetime" timestamp,
  "product_price" float,
  "total_price" float,
  "customer_alias" varchar,
  "country" varchar,
  "source_file" varchar,
  "creation_datefile" date,
  "created_at" timestamp
);

CREATE TABLE "products" (
  "product_id" integer PRIMARY KEY,
  "product_description" varchar,
  "product_price" float,
  "source_file" varchar,
  "created_at" timestamp,
  "update_at" timestamp
);

CREATE TABLE "customers" (
  "customer_id" varchar PRIMARY KEY,
  "customer_alias" varchar,
  "source_file" varchar,
  "created_at" timestamp,
  "update_at" timestamp
);

ALTER TABLE "transactions" ADD FOREIGN KEY ("product_id") REFERENCES "products" ("product_id");

ALTER TABLE "transactions" ADD FOREIGN KEY ("customer_alias") REFERENCES "customers" ("customer_alias");
