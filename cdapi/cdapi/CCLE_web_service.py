from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from cdapi.CCLEData import CCLEData

"""
Load the data
"""
data = CCLEData('data/ccle_data_short.csv')

description = """
Welcome to the Cancer Data API. With the API you can do the following
tasks:
* Discover whether a given gene is a TCGA hotspot for a given cell line
* Get the list of TCGA hotspot genes for a given cell line
* Get the list of cell lines that a given gene is a TCGA hotspot for
"""

"""
This is the web service.
"""
app = FastAPI(
    title="Cancer Data API",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Jay Jay Billings",
        "url": "https://www.jayjaybillings.com",
        "email": "jayjaybillings@gmail.com",
    },
    license_info={
        "name": "New BSD License",
        "url": "https://opensource.org/license/BSD-3-clause/",
    },
)

@app.get("/", response_class=HTMLResponse)
async def root():
    page_html = """
        <html>
            <head><title>Cancer Data API</title></head>
            <body>
                <p>Welcome to the cancer data API web service. This
                page is a stub, and more information is available in
                the <a href="docs/">documentation</a>. The docs are
                also available in the <a href="redoc/">redoc format</a>.
                Finally, an <a href="openapi.json">OpenAPI-compliant
                schema</a> is available.
            </body>
        </html>
    """
    return page_html

@app.get("/checkHotspot/")
async def check_hotspot(gene_id : int, cell_line : str):
    """ This function checks whether the named gene is a TCGA
    hotspot for the name cell line.

    Parameters
    ----------
    gene_id : int

        The Entrez Gene Id of the gene to check in the cell line

    cell_line : str

        The DepMap_ID of the cell line that make have the hotspot
        gene

    Return
    ------
    True if the gene is a TCGA hotspot gene in the cell line, and
    False if not.
    """
    return {"isTCGAHotspot",data.is_tcga_hotspot(gene_id,cell_line)}

@app.get("/genes/{cell_line}")
async def get_genes(cell_line : str):
    """ This function returns the tcga hotspot genes for the given
    cell line, if they exist. If not, it returns None.

    Parameters
    ----------
    cell_line : str

        The name of the cell line

    Return
    ------
    genes : json

        The json list of tcga hotspot genes in the cell line. Empty if
        the cell_line isn't found ([]).

    """
    gene_list = jsonable_encoder(data.get_tcga_genes(cell_line))
    return JSONResponse(content=gene_list)

@app.get("/cell_lines/{genes}")
async def get_cell_lines(gene : int):
    """ This function returns all available cell lines for a given
    gene, if they exist.

    Parameters
    ----------
    gene : str

        The name of the gene

    Returns
    -------
    list : json

        A json list of the cell lines for the gene if it exists.
        Otherwise this function returns an empty json list ([]).

    """
    cell_line_list = jsonable_encoder(data.get_cell_lines(gene))
    return JSONResponse(content=cell_line_list)