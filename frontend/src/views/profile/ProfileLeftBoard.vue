<template>
	<div class="main-left col-span-1 space-y-4">
		<div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
			<img
				src="https://i.pravatar.cc/300?img=70"
				class="mb-6 rounded-full" />

			<p>
				<strong>{{ profile.name }}</strong>
			</p>
			<div class="mt-6 flex space-x-8 justify-around">
				<p class="text-xs text-gray-500">182 friends</p>
				<p class="text-xs text-gray-500">120 posts</p>
			</div>
		</div>
		<MyPendingRequests v-if="isMyProfile" />
		<MyFriends v-if="isMyProfile" />
		<SendRequest
			v-if="isLoading === false"
			:isFriend="isFriend"
			:isRequestPending="isRequestPending" />
	</div>
</template>

<script>
	// import MyPendingRequests from '@/components/friendship/PendingRequests.vue';
	// import MyFriends from '../../components/friendship/MyFriends.vue';

	export default {
		setup() {
			return {};
		},
	};
</script>

<style lang="scss" scoped></style>
