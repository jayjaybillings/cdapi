# Cancer Data API Project for Zephyr AI job interview

This is a simple API that provides a RESTful (mostly...) API to query the cellular model mutations dataset from the Cancer Dependency Map. It uses a compressed version of the dataset to show only those genes that are marked as hotspots in the Cancer Genome Atlas (TCGA). Entrez gene ids identify genes and DepMap ids identify cell lines.

Genes can be checked against cell lines to see if they are considered TCGA hotspot genes. Genes can also be searched to return the full list of cell lines where they are considered hotspots. Finally, cell lines can be queried to get all genes that are hotspots for that line.

The service can be run locally or in a Docker container.

## Quick start

The project is split in code and Docker directories. Follow instructions in [cdapi/README.md](cdapi/README.md) to start the API in standalone mode. Follow the instructions in [cdapi_docker/README.md](cdapi_docker/README.md) to create and launch the Docker container.

Developer instructions are also available in [cdapi/README.md](cdapi/README.md).

## License and Copyright

See [LICENSE](License).