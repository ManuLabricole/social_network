<template>
	<div class="main-left col-span-1 space-y-4">
		<div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
			<img
				src="https://i.pravatar.cc/300?img=70"
				class="mb-6 rounded-full" />

			<p>
				<strong>{{ profile.user.name }}</strong>
			</p>
			<div class="mt-6 flex space-x-8 justify-around">
				<p class="text-xs text-gray-500">
					{{ profile.number_of_friends }}
					{{ profile.number_of_friends === 1 ? 'friend' : 'friends' }}
				</p>
				<p class="text-xs text-gray-500">120 posts</p>
				<p
					v-if="!isMyProfile"
					class="text-xs text-gray-500">
					button add or remove
				</p>
			</div>
		</div>
		<MyPendingRequests v-if="isMyProfile" />
		<Friends v-if="isMyProfile" />
		<!--
		<SendRequest
			v-if="isLoading === false"
			:isFriend="isFriend"
			:isRequestPending="isRequestPending" /> 
		--></div>
</template>

<script>
	import MyPendingRequests from '../../components/friendship/MyPendingRequests.vue';
	import Friends from '../../components/friendship/Friends.vue';
	import axios from 'axios';

	export default {
		name: 'ProfileLeftBoard',
		components: {
			MyPendingRequests,
			Friends,
		},
		setup() {
			return {};
		},
		props: {
			profile: {
				type: Object,
				required: true,
			},
			isMyProfile: {
				type: Boolean,
				required: true,
			},
		},
		mounted() {
			if (this.isMyProfile) {
				// this.getFriendRequestStatus();
			} else {
				this.isLoading = false;
				// console.log('not my profile');
			}
			// console.log('profile left board mounted', this.profile);
			console.log('mounted() isMyProfile: ', this.isMyProfile);
		},
		methods: {
			// getFriendRequestStatus() {
			// 	// console.log('getFriendRequestStatus');
			// 	axios
			// 		.get(`/api/v1/friend-requests/check-friendship/${this.profile.id}/`)
			// 		.then((response) => {
			// 			// console.log(response.data.response);
			// 			this.isFriend = response.data.response.is_friend;
			// 			this.isRequestPending = response.data.response.is_request_pending;
			// 			this.isLoading = false;
			// 		})
			// 		.catch((error) => {
			// 			console.error(error);
			// 			console.warn('Error getting relation status');
			// 			this.isLoading = false;
			// 		});
			// },
		},
	};
</script>
