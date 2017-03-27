from src import job

jobDescription = {
	"jobName": "branching",
	"inputsDef": [
		{ "name": "code", "type": "series", "length": 25, "depth": 3, "mutationRate": 0.5}
		],
	"outputsDef": [
		{ "name": "width1", "type": "objective", "goal": "min"},
		{ "name": "width2", "type": "objective", "goal": "min"},
		{ "name": "height", "type": "objective", "goal": "min"}
		],
	"algo": "GA",
	"algoOptions": {
		"numGenerations": 50,
		"numPopulation": 50,
		"mutationRate": 0.05,
		"saveElites": 5
		},
	"jobOptions": {
		"screenshots": True
		}
	}

# job.createInputFile(jobDescription)
job.run(jobDescription)