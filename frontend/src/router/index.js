import { loadLayout, loadView } from "@/composables/utils"
import { createRouter, createWebHistory } from "vue-router"

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: loadLayout('BaseDashboard'),
      children: [
        {
          path: '',
          name: 'home_view',
          component: loadView('IndexView'),
          meta: {
            title: 'Index'
          }
        },
        {
          path: 'campaigns',
          name: 'campaigns_view',
          component: loadView('CampaignsView'),
          meta: {
            title: 'Campaigns'
          }
        },
        {
          path: 'campaigns/setup/',
          component: loadLayout ('CampaignsLayout'),
          children: [
            // {
            //   path: '',
            //   name: 'list_campaigns_setup_view',
            //   component: loadView('setup/ListCampaignsView')
            // },
            {
              path: ':id(\\d+)',
              name: 'campaign_setup_view',
              component: loadView('setup/CampaignSetupView'),
              meta: {
                title: 'Create campaign'
              }
            },
            {
              path: ':id(\\d+)/settings',
              name: 'campaign_setup_settings_view',
              component: loadView('setup/CampaignSettingsView'),
              meta: {
                title: 'Campaign settings'
              }
            }
          ]
        },
        {
          path: 'queue',
          name: 'queue_view',
          component: loadView('QueueView'),
          meta: {
            title: 'Queue'
          }
        }
      ]
    }
  ]
})

export default router
