<template>
	<div
		v-if="isProfileFetched"
		class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
		<profile-left-board
			:profile="profile"
			:isMyProfile="isMyProfile" />
		<profile-middle-feed :profile="profile" />
		<profile-right-suggestions :profile="profile" />
	</div>
</template>

<script>
	import ProfileLeftBoard from './ProfileLeftBoard.vue';
	import ProfileMiddleFeed from './ProfileMiddleFeed.vue';
	import ProfileRightSuggestions from './ProfileRightSuggestions.vue';

	import { useUserStore } from '@/stores/user';
	import axios from 'axios';

	export default {
		name: 'ProfileView',
		components: {
			ProfileLeftBoard,
			ProfileMiddleFeed,
			ProfileRightSuggestions,
		},
		props: {
			id: {
				type: String,
				required: true,
			},
		},
		data() {
			return {
				userStore: useUserStore(),
				isMyProfile: false,
				isProfileFetched: false,
				profile: null,
			};
		},
		mounted() {
			this.fetchProfile();
		},
		methods: {
			fetchProfile() {
				console.log('fetchProfile()', this.id);
				const endpoint =
					this.id === this.userStore.user.id
						? '/api/v1/users/me/'
						: `/api/v1/users/${this.id}/`;

				axios
					.get(endpoint)
					.then((response) => {
						this.profile = response.data;
						this.setIsMyProfile();
						this.isProfileFetched = true;
					})
					.catch((error) => {
						console.error(error);
						console.warn('Error getting profile');
					});
			},
			setIsMyProfile() {
				if (this.profile && this.profile.user.id === this.userStore.user.id) {
					this.isMyProfile = true;
					console.log('setIsMyProfile() isMyProfile: ', this.isMyProfile);
				} else {
					this.isMyProfile = false; // Ensure it's set to false if conditions aren't met
				}
			},
		},
		watch: {
			id() {
				this.isProfileFetched = false;
				this.fetchProfile();
			},
		},
	};
</script>
