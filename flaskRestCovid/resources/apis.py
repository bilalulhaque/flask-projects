from flask_restful import Resource, reqparse, abort
import json
from flask_jwt_extended import jwt_required


f = open('resources/owid-covid-data.json')
data = json.load(f)

#For POST
country_post_args = reqparse.RequestParser()
country_post_args.add_argument("date", type=str, required=True)
country_post_args.add_argument("total_cases", type=float, required=True)
country_post_args.add_argument("new_cases", type=float, required=True)
country_post_args.add_argument("total_cases_per_million", type=float, required=True)
country_post_args.add_argument("new_cases_per_million", type=float, required=True)
country_post_args.add_argument("stringency_index", type=float, required=True)


#For PUT
country_put_args = reqparse.RequestParser()
country_put_args.add_argument("continent", type=str)
country_put_args.add_argument("location", type=str)
country_put_args.add_argument("population", type=int)
country_put_args.add_argument("population_density", type=float)
country_put_args.add_argument("median_age", type=float)
country_put_args.add_argument("aged_65_older", type=float)
country_put_args.add_argument("aged_70_older", type=float)
country_put_args.add_argument("gdp_per_capita", type=float)
country_put_args.add_argument("cardiovasc_death_rate", type=float)
country_put_args.add_argument("diabetes_prevalence", type=float)
country_put_args.add_argument("handwashing_facilities", type=float)
country_put_args.add_argument("hospital_beds_per_thousand", type=float)
country_put_args.add_argument("life_expectancy", type=float)
country_put_args.add_argument("human_development_index", type=float)



class CountryData(Resource):
    @jwt_required()
    def get(self, iso_code):
        return data[iso_code], 200

    @jwt_required()
    def post(self, iso_code):
        args = country_post_args.parse_args()
        if iso_code not in data:
            abort(409, message="Not present")
        data[iso_code]['data'].append({"date": args["date"], "total_cases": args["total_cases"], "new_cases": args["new_cases"], "total_cases_per_million": args["total_cases_per_million"], "new_cases_per_million": args["new_cases_per_million"], "stringency_index": args["stringency_index"]})

        with open("resources/owid-covid-data.json", "w") as jsonFile:
            json.dump(data, jsonFile)

        return data[iso_code]['data'], 200

    @jwt_required()
    def put(self, iso_code):
        args = country_put_args.parse_args()
        if iso_code not in data:
            abort(409, message="Not present")

        if args['continent']:
            data[iso_code]['continent'] = args['continent']
        if args['location']:
            data[iso_code]['location'] = args['location']
        if args['population']:
            data[iso_code]['population'] = args['population']
        if args['population_density']:
            data[iso_code]['population_density'] = args['population_density']
        if args['median_age']:
            data[iso_code]['median_age'] = args['median_age']
        if args['aged_65_older']:
            data[iso_code]['aged_65_older'] = args['aged_65_older']
        if args['aged_70_older']:
            data[iso_code]['aged_70_older'] = args['aged_70_older']
        if args['gdp_per_capita']:
            data[iso_code]['gdp_per_capita'] = args['gdp_per_capita']
        if args['cardiovasc_death_rate']:
            data[iso_code]['cardiovasc_death_rate'] = args['cardiovasc_death_rate']
        if args['diabetes_prevalence']:
            data[iso_code]['diabetes_prevalence'] = args['diabetes_prevalence']
        if args['handwashing_facilities']:
            data[iso_code]['handwashing_facilities'] = args['handwashing_facilities']
        if args['hospital_beds_per_thousand']:
            data[iso_code]['hospital_beds_per_thousand'] = args['hospital_beds_per_thousand']
        if args['life_expectancy']:
            data[iso_code]['life_expectancy'] = args['life_expectancy']
        if args['human_development_index']:
            data[iso_code]['human_development_index'] = args['human_development_index']
        return data[iso_code], 200

    @jwt_required()
    def delete(self, iso_code):
        del data[iso_code]
        return 'Deleted', 200

class CountryDataDate(Resource):
    @jwt_required()
    def get(self, iso_code, date):
        all_dates = data[iso_code]['data']
        for i in range(len(all_dates)):
            for key, value in all_dates[i].items():
                if value == date:
                    return all_dates[i], 200
