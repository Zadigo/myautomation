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
            title: 'Index',
            showLink: true
          }
        },
        {
          path: 'campaigns',
          name: 'campaigns_view',
          component: loadView('CampaignsView'),
          meta: {
            title: 'Campaigns',
            showLink: true
          }
        },
        {
          path: 'campaign/:id(\\d+)',
          name: 'campaign_view',
          component: loadView('CampaignView'),
          meta: {
            title: 'Campaign',
            showLink: true
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
                title: 'Create campaign',
                requiresPremium: true
              }
            },
            {
              path: ':id(\\d+)/custom-setup',
              name: 'custom_campaign_setup_view',
              component: loadView('setup/CustomCampaignSetupView'),
              meta: {
                title: 'Custom campaign settings',
                requiresPremium: true
              }
            },
            {
              path: ':id(\\d+)/settings',
              name: 'campaign_setup_settings_view',
              component: loadView('setup/CampaignSettingsView'),
              meta: {
                title: 'Campaign settings',
                requiresPremium: false
              }
            }
          ]
        },
        {
          path: 'queue',
          name: 'queue_view',
          component: loadView('QueueView'),
          meta: {
            title: 'Queue',
            showLink: false
          }
        }
      ]
    }
  ]
})

export default router
