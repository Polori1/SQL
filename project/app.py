from sqlmodel import Session, select

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

        oficina_ventas = Oficina(
            nombre="Ventas",
            direccion="Av. General Paz 120"
         )

        persona_miguel = Persona(
            nombre="Miguel Perez",
            edad=35,
            direccion="Ensenada 2365",
            oficina=oficina_admin
        )

        persona_juan = Persona(
            nombre="Juan Gomez",
            edad=28,
            direccion="Santa Rosa 450",
            oficina=oficina_admin
        )

        persona_ana = Persona(
            nombre="Ana Lopez",
            edad=31,
            direccion="La Rioja 800",
            oficina=oficina_ventas
        )

        session.add(persona_miguel)
        session.add(persona_juan)
        session.add(persona_ana)
        session.commit()
        
        print("Personas creadas correctamente.")

        session.refresh(persona_miguel)

        print("Persona Creada:", persona_miguel)
        print("Su oficina:", persona_miguel.oficina)

def listar_personas_oficina(oficina_id):
    with Session(engine) as session:
        oficina = session.get(Oficina, oficina_id)

        if oficina:
            print(f"\nPersonas de la oficina {oficina.nombre}:")

            for persona in oficina.personas:
                print(f"- {persona.nombre}")
        else:
            print("Oficina no encontrada.")

def consulta_join():
    with Session(engine) as session:
        resultados = session.exec(
            select(Persona.nombre, Oficina.nombre)
            .join(Oficina)
        ).all()

        print("\nPersonas y sus oficinas:")

        for persona, oficina in resultados:
            print(f"- {persona} trabaja en {oficina}")

def buscar_personas_por_edad(edad):
    with Session(engine) as session:
        resultados = session.exec(
            select(Persona).where(Persona.edad >= edad)
        ).all()

        print(f"\nPersonas con {edad} años o más:")

        for persona in resultados:
            print(f"- {persona.nombre} ({persona.edad} años)")

def reasignar_persona(persona_id, nueva_oficina_id):
    with Session(engine) as session:
        persona = session.get(Persona, persona_id)
        nueva_oficina = session.get(Oficina, nueva_oficina_id)

        if persona and nueva_oficina:
            persona.oficina = nueva_oficina

            session.add(persona)
            session.commit()
            session.refresh(persona)

            print(
                f"\n{persona.nombre} fue reasignado a "
                f"{nueva_oficina.nombre}."
            )
        else:
            print("Persona u oficina no encontrada.")

def eliminar_persona(persona_id):
    with Session(engine) as session:
        persona = session.get(Persona, persona_id)

        if persona:
            session.delete(persona)
            session.commit()
            print(f"\nPersona {persona.nombre} eliminada.")
        else:
            print("Persona no encontrada.")

def eliminar_oficina(oficina_id):
    with Session(engine) as session:
        oficina = session.get(Oficina, oficina_id)

        if oficina:
            session.delete(oficina)
            session.commit()
            print(f"\nOficina {oficina.nombre} eliminada.")
        else:
            print("Oficina no encontrada.")


def main():
    create_db_and_tables()
    create_personas()
    listar_personas_oficina(1)
    consulta_join()
    buscar_personas_por_edad(30)
    reasignar_persona(1,2)
    eliminar_persona(3)
    eliminar_oficina(2)


if __name__ == "__main__":
    main()
