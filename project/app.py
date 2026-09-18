from sqlmodel import Session

from .database import create_db_and_tables, engine
from .models import Persona, Oficina


def create_personas():
    with Session(engine) as session:
        oficina_admin = Oficina(
            nombre="Administracion", 
            direccion="Av. Colon 348"
        )
        #session.add(oficina_admin)
        #session.commit()

        persona_miguel = Persona(
            nombre="Miguel Perez", 
            direccion="Ensenada 2365", 
            oficina=oficina_admin
        )
        session.add(persona_miguel)
        session.commit()

        session.refresh(persona_miguel)

        print("Persona Creada:", persona_miguel)
        print("Su oficina:", persona_miguel.oficina)


def main():
    create_db_and_tables()
    create_personas()


if __name__ == "__main__":
    main()
