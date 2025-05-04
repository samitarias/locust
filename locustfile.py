from locust import HttpUser, task, between

class TranslatorApiUser(HttpUser):
    wait_time = between(1, 3)  # tiempo de espera entre tareas (segundos)

    @task
    def get_translation(self):
        url = "/translatorApi/codeTranslation"
        params = {
            "name1": "IdentificationType",
            "esp": "TECH",
            "sp": "NSBT",
            "unpaged": "true"
        }
        self.client.get(url, params=params, name="Get codeTranslation")

    def on_start(self):
        # Esto se ejecuta una vez por usuario al iniciar
        print("Iniciando usuario de prueba para Translator API")
