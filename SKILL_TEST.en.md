Please answer the following coding question.

# Coding question
You are member of SRE team who need to review lots of Kubernetes config yaml files(details about Kubernetes yamls can be checked on the internet) in your daily tasks.
These yaml file configures the applications or container deployment configurations.
Example yaml files for Kubernetes resources
- https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#creating-a-deployment
- https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/#create-a-daemonset
- https://kubernetes.io/docs/concepts/services-networking/service/#defining-a-service
- Sample yamls files are in [example_yamls](./example_yamls/) folder

Now there are some rules created by SRE team for best practices and governance.
Example :-
- `spec.replicas` should be at least 3 in production environment
- `metadata.labels` should contain a key called `app` and value `{app_name}`
- If `kind` is `Service` then `spec.ports` should have at least one port in the list

Similarly there can be many rules which are mandatory and while reviewing you need to carefully see and verify to make sure that all yamls files are following the rules.

This review task takes huge time and we need to automate this by having some lint rules from which we can autocheck the yaml files when someone raises any pull request on GitHub.

## Task
Write code and README considering below inputs and outputs.

### Input: Mainly 3 inputs needs to be considered
1. Path of yaml file or directory which has yaml files
	- Path can be anything from below
		 - Single yaml file path
		 - Single file path with multiple yamls separated by “---” \
     Example :- [example-2.yaml](example_yamls/example-2.yaml)
		- Directory path which has yaml files (directory may have other files also like *.txt)
  		- Directory path which has nested directories which has yaml files
2. Input Key String which need to be searched in yaml files\
    Example :-
    - `apiVersion` <- simple key
    - `spec.replicas` <- dot means nested keys in dictionary
    - `spec.ports[0].name` <- bracket means ports is a list, and 0 inside bracket means first element of ports list, [0].name means “name” key of first element in ports list
    - `spec.ports[*].name`  <-  bracket means ports is a list, and * inside bracket means all element of ports list, [*].name means “name” key of all element in ports list

3. Value to be matched against the key given in 2nd input\
    Example :-
      - `100%`  <- String
      - `2`  <- Integer


### Output: Print 3 comma separated columns on console
1. First column should have the key which matched in yaml file, If key is `port[*].name` print all ports which exists in separate line.\
Example :-
    - If key is `port[*].name` and there are 3 ports, then first output column will be like below
      - `key = port[0].name`
      - `key = port[1].name`
      - `key = port[2].name`
2. Second column should have the value which matched with the key in yaml, If key is `port[*].name` and value is `HTTP` print all ports which exists in separate line.\
Example :-
    - If key is `port[*].name`, value is `HTTP` and there are 3 ports, then first and second output column will be like below
      - `key = port[0].name`, `value = HTTP`
      - `key = port[1].name`, `value = HTTP`
      - `key = port[2].name`, `value = HTTP`
3. Third column should have relative file path in which the input key and value were matched.

### Sample Input and output:

#### Example-1
##### Input
```
# input file_name key value (this line is comment)
deploy-to-dev.yaml apiVersion batch/v1
```
##### Output
```
key = apiVersion, value = batch/v1, deploy-to-dev.yaml
```
#### Example-2
##### Input
```
# input directory_name key value (this line is comment)
serviceA/production metadata.namespace service-a
```
##### Output
```
key = metadata.namespace, value = service-a, serviceA/production/deploy-to-prod.yaml
key = metadata.namespace, value = service-a, serviceA/production/deploy-to-canary.yaml
```
#### Example-3
##### Input
```
# <input directory which has multiple yamls> key value
serviceA/test spec.ports[*].name http
```
##### Output
```
key = spec.ports[0].name, value = http, serviceA/test/deploy-to-test.yaml
key = spec.ports[3].name, value = http, serviceA/test/deploy-to-test.yaml
key = spec.ports[0].name, value = http, serviceA/test/deploy-to-qa.yaml
```

## Important things
- Your program should be well documented so that third person can understand what you are doing
- Consider your source code will be used by automation team to check different rules. So split the code accordingly by which anyone can use only specific part of your code
- You are free to use open source libraries and tools inside your code
- Prepare a proper **Dockerfile** and **README** from which evaluator can test your code on his machine (If you are installing any custom libraries or packages include them in Dockerfile, so that the evaluator can use your Dockerfile and run your code)
- You can choose any programming language from these (Shell, Go, Python, Ruby), but readme should have info "**How to run from scratch**"
- This is an open ended question, feel free to put more thoughts and implementation as an SRE member
- All documentation and README should be in english

### Additional : Only if you have extra time and interest
- Implement matching using regex, in above task you have to match exact key and value. Try to match using regex option also.
- Additional ideas of improving this parser and automating the whole review process.

