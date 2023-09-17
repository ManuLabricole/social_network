import { defineStore } from 'pinia'
import axios from 'axios'

// Define a Pinia store for managing user authentication and data.
export const useUserStore = defineStore('user', {

    state: () => ({
        user: {
            isAuthenticated: false, // Flag indicating user authentication status.
            id: null,               // User ID.
            name: null,             // User's name.
            email: null,            // User's email.
            access: null,           // Access token.
            refresh: null,          // Refresh token.
        }
    }),

    actions: {
        // Action to initialize the store based on locally stored authentication tokens.
        initStore() {
            console.log('initStore', localStorage.getItem('user.access'))

            if (localStorage.getItem('user.access')) {
                // console.log('User has access!')

                // Retrieve and set user data from local storage.
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.id = localStorage.getItem('user.id')
                this.user.name = localStorage.getItem('user.name')
                this.user.email = localStorage.getItem('user.email')
                this.user.isAuthenticated = true

                // Refresh the access token.
                this.refreshToken()
                // console.info('Initialized user:', this.user)
            }
        },

        // Action to set user authentication tokens and update the store.
        setToken(data) {

            // Set user tokens and update authentication status.
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            // Store tokens in local storage.
            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)

        },

        // Action to remove user authentication tokens and clear user data.
        // Call when we logout.
        removeToken() {
            console.log('removeToken')

            // Clear tokens and reset authentication status.
            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = null
            this.user.name = null
            this.user.email = null

            // Clear token data from local storage.
            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.isAuthenticated', false)
        },

        // Action to set user information and store it in local storage.
        setUserInfo(user) {

            // Set user information.
            this.user.id = user.id
            this.user.name = user.name
            this.user.email = user.email
            this.user.isAuthenticated = true

            // Store user information in local storage.
            localStorage.setItem('user.id', this.user.id)
            localStorage.setItem('user.name', this.user.name)
            localStorage.setItem('user.email', this.user.email)
            localStorage.setItem('user.isAuthenticated', this.user.isAuthenticated)

        },

        // Action to refresh the access token using the refresh token.
        refreshToken() {
            axios.post('/api/v1/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    // Update the access token.
                    this.user.access = response.data.access

                    // Store the updated access token in local storage.
                    localStorage.setItem('user.access', response.data.access)

                    // Set the authorization header for Axios to use the new access token.
                    // Mind the space after "Bearer"!
                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error) => {
                    console.log(error)

                    // If token refresh fails, remove user tokens and log the user out.
                    this.removeToken()
                })
        },
    }
})
