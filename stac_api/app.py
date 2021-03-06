"""FastAPI application."""
from stac_api.api.app import StacApi
from stac_api.api.extensions import (
    BulkTransactionExtension,
    FieldsExtension,
    QueryExtension,
    SortExtension,
    TilesExtension,
    TransactionExtension,
)
from stac_api.clients.postgres.core import CoreCrudClient
from stac_api.clients.postgres.session import Session
from stac_api.clients.postgres.transactions import (
    BulkTransactionsClient,
    TransactionsClient,
)
from stac_api.clients.tiles.ogc import TilesClient
from stac_api.config import PostgresSettings

settings = PostgresSettings()
session = Session(settings.reader_connection_string, settings.writer_connection_string)
api = StacApi(
    settings=settings,
    extensions=[
        TransactionExtension(client=TransactionsClient(session=session)),
        BulkTransactionExtension(client=BulkTransactionsClient(session=session)),
        FieldsExtension(),
        QueryExtension(),
        SortExtension(),
        TilesExtension(TilesClient(session=session)),
    ],
    client=CoreCrudClient(session=session),
)
app = api.app
