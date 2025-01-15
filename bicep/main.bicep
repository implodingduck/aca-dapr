param location string = resourceGroup().location

resource aca_env 'Microsoft.App/managedEnvironments@2024-03-01' existing = {
  name: 'ace-internal-only'
}

resource service 'Microsoft.App/containerApps@2024-03-01' = {
  name: 'differentsubacr'
  location: location
  properties: {
    environmentId: aca_env.id
    workloadProfileName: 'Consumption'
    configuration: {
      ingress: {
        external:false
        targetPort: 80
      }
      registries: [
        {
          server: 'abc768254acr.azurecr.io'
          identity: '/subscriptions/xxxxxxxx-yyyy-zzzz-aaaa-bbbbbbbbbbbb/resourceGroups/rg-quackers-bank-xyz123-eastus/providers/Microsoft.ManagedIdentity/userAssignedIdentities/uai-aca-to-acr'
        }
      ]
    }
    template: {
      containers: [
        {
          name: 'differentsubacr'
          image: 'abc768254acr.azurecr.io/aca-dapr-basic:latest'
          resources: {
            cpu: '0.5'
            memory: '1Gi'
          }
          
        }
      ]
    }
  }
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '/subscriptions/xxxxxxxx-yyyy-zzzz-aaaa-bbbbbbbbbbbb/resourceGroups/rg-quackers-bank-xyz123-eastus/providers/Microsoft.ManagedIdentity/userAssignedIdentities/uai-aca-to-acr' : {}
    }
  }
}
