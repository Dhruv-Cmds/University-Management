from pydantic import StringConstraints
from typing import Annotated

NameStr = Annotated[str, 
                        StringConstraints(
                            min_length=2, 
                            max_length=100
                            )
                    ]

PhoneStr = Annotated[str, 
                        StringConstraints(
                            min_length=10,
                            max_length=20
                        )
                    ]

CourseStr = Annotated[str, 
                        StringConstraints(
                            min_length=2, 
                            max_length=100
                            )
                    ]