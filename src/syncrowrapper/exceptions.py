class MissingParametersException(Exception):
    def __init__(
        self,
        missing_parameters: str | list[str] | None = None,
    ):
        if isinstance(missing_parameters, str):
            missing_parameters = [missing_parameters]
        self.message = 'Missing unspecified required parameters!'
        if missing_parameters is not None:
            self.message = (
                'Missing the following required parameters:\n'
                + '\n'.join([f'\t{x}' for x in missing_parameters])
            )
        super().__init__(self.message)
