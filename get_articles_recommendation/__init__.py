import azure.functions as func
import logging

def get_articles_recommendation(articles: func.DocumentList) -> func.Document:
    """Cette fonction retourne les éléments de la liste des recommandations"""
    if not articles or not len(articles):
        logging.warning('Aucun élément de recommandation trouvé')
        raise Exception('Aucun élément de recommandation trouvé')
    return articles[0]

def main(req: func.HttpRequest, articles: func.DocumentList) -> func.HttpResponse:
    """Cette fonction est l'entrée principale de l'application 
    et retourne une réponse HTTP en fonction des éléments de recommandation passés en paramètre
    """
    logging.info('Demande HTTP reçue.')

    try:
        article = get_articles_recommendation(articles)
    except Exception as e:
        logging.error(e)
        return func.HttpResponse(
            str(e),
            status_code=404,
        )

    return func.HttpResponse(
        article.to_json(),
        mimetype='application/json',
        status_code=200,
    )