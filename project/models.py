from sqlmodel import Field, Relationship, SQLModel


class Oficina(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    direccion: str

    personas: list["Persona"] = Relationship(back_populates="oficina")


class Persona(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)    
    edad: int | None = Field(default=None, index=True)
    direccion: str

    oficina_id: int | None = Field(default=None, foreign_key="oficina.id")
    oficina: Oficina | None = Relationship(back_populates="personas")
