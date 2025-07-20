import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("payment.avsc", "rb").read())

reader = DataFileReader(open("sample-payment.json", "rb"), DatumReader)
for payment in reader:
    print(payment)

reader.close()

writer = DataFileWriter(open("sample-payment-2.json", "wb"), DatumWriter(), schema)
writer.append({"unique-id": "2222","payment-date:": "2025-07-20","amount": "10.00", "currency": "GBP", \
    "scheme": "MASTERCARD", "card-holder-details": {"name": "Simon Taylor", "location": "London"}})

writer.close()


