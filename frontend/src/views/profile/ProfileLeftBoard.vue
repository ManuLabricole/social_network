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
		<div class="flex align-center">
			<SendRequest
				v-if="!isMyProfile"
				:profile="profile" />
			<p>message</p>
		</div>
	</div>
</template>

<script>
	import MyPendingRequests from '../../components/friendship/MyPendingRequests.vue';
	import Friends from '../../components/friendship/Friends.vue';
	import SendRequest from '../../components/friendship/SendRequest.vue';
	import axios from 'axios';

	export default {
		name: 'ProfileLeftBoard',
		components: {
			MyPendingRequests,
			Friends,
			SendRequest,
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
	};
</script>
