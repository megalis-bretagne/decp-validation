import json
import argparse
from jsonschema import Draft202012Validator
schema_file = "schema_decp_v2.0.2.json"

def validate_json(json_file):
    """
    Valide un fichier JSON par rapport à un schéma JSON et liste les erreurs de validation.

    :param json_file: Chemin vers le fichier JSON à valider.
    :return: Liste des erreurs de validation, s'il y en a.
    """
    # Lire le fichier JSON
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Lire le schéma JSON
    with open(schema_file, 'r') as f:
        schema = json.load(f)
    
    # Liste pour stocker les erreurs de validation
    errors = []
    
    # Valider le JSON par rapport au schéma
    #validate(instance=data, schema=schema, format_checker=Draft202012Validator.FORMAT_CHECKER,)
    v = Draft202012Validator(schema)
    errors = v.iter_errors(data)
    # errors = sorted(v.iter_errors(data), key=lambda e: e.path)

    return errors

def main():
    parser = argparse.ArgumentParser(description='Valide un fichier JSON par rapport à un schéma JSON.')
    parser.add_argument('json_file', help='Chemin vers le fichier JSON à valider.')

    args = parser.parse_args()
    
    erreurs = validate_json(args.json_file)
    if erreurs:
        print("Erreurs de validation :")
        for erreur in erreurs:
            print(f"{erreur.message} as {erreur.json_path}")
    else:
        print("Le fichier JSON est valide par rapport au schéma.")

if __name__ == "__main__":
    main()
