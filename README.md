Current flow available:
1.	Voice Input: The SAP customer uses voice input to describe the desired custom code functionality
2.	Code Generation. The LLM (Language Model) from Azure Open AI API, specifically the GPT-4-32k model, auto-generates the code based on their input.
3.	Code Update: the customer's client code automatically updates to the custom code.
4.	Restoration after Version Update : During a version update, the custom code gets overwritten by standard code. Upon discovery, the customer implements a restoration of their custom code.

Next steps:
1.	Annotation Addition The customer notices the generated code lacks annotations. They use the LLM again to add the necessary annotations (Faye)
2.	Code Review and Update: The customer tells LLM the code is satisfactory, the customer's client code automatically updates to the custom code. (Faye)
3.	Confirmation before restoration: when detecting the customized code overwritten in new version, a confirmation is needed from customer for restoration(Faye)
4.	Trigger point to invoke enhancement point ( TBD)
5.	Customization code result display (TBD)


a. check if customization code still applicable with the new version of SAP products

Obtain the update content of the cloud product from update logs or API documentation.
Use a Language Model (LLM) to understand the semantics of the updates.
Translate the LLM's understanding into the specific impact on your custom code.
Use these impacts to check the compatibility of your custom code with the cloud product updates.
Modify your code if any incompatibilities are found to adapt to the new version of the cloud product.
