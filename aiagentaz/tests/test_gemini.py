from aiagentaz.domain.agent import Agent


if __name__ == "__main__":
    
    my_agent = Agent(
        client="gemini", 
        api_key="AIzaSyAeawtcCKK8_d2-HNPuSzIIidf3Ho9nQyI"
    )
    res = my_agent.generate( 
        model="gemini-1.5-flash", 
        prompt="Can you give me a hello world program in python?", 
    )

    print(res)