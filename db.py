import aiohttp
from models import Session, SwapiPeople


async def get_data(client, data, param: str):
    if isinstance(data, list):
        data_list = []
        for url_ in data:
            async with client.get(url_) as response:
                json_data = await response.json()
                data_list.append(json_data[f'{param}'])
        return data_list
    else:
        async with client.get(data) as response:
            new_data = await response.json()
        return new_data[f'{param}']
        
        
async def paste_to_db(people_json):
    async with aiohttp.ClientSession() as client:
        async with Session() as session:
            try:
                objects = [SwapiPeople(
                                    birth_year=hero['birth_year'],
                                    eye_color=hero['eye_color'],
                                    films=', '.join(await get_data(client, hero['films'], param='title')),
                                    gender=hero['gender'],
                                    hair_color=hero['hair_color'],
                                    height=hero['height'],
                                    homeworld=await get_data(client, hero['homeworld'], param='name'),
                                    mass=hero['mass'],
                                    name=hero['name'],
                                    skin_color=hero['skin_color'],
                                    species=', '.join(await get_data(client, hero['species'], param='name')),
                                    starships=', '.join(await get_data(client, hero['starships'], param='name')),
                                    vehicles=', '.join(await get_data(client, hero['vehicles'], param='name'))
                                    )
                                    for hero in people_json
                                    ]
                session.add_all(objects)
            except KeyError as err:
                pass
            await session.commit()
        