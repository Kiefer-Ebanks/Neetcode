func search(nums []int, target int) int {
    j := (len(nums)-1)
    i := 0

    for i <= j{
        
        mid := i + (j - i)/2

        if nums[mid] == target {
            return mid
        } else if nums[mid] > target {
            j = mid - 1
        } else {
            i = mid + 1
        }
        
    }

    return -1
}
