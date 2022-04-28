class UnknownErrorHasOccurred(BaseException):
    pass


class TheApplicationIsDisabled(BaseException):
    pass


class UnknownMethodPassed(BaseException):
    pass


class InvalidSignature(BaseException):
    pass


class UserAuthorizationFailed(BaseException):
    pass


class TooManyRequestsPerSecond(BaseException):
    pass


class YouDoNotHavePermissionToPerformThisAction(BaseException):
    pass


class InvalidRequest(BaseException):
    pass


class TooManySimilarActions(BaseException):
    pass


class AnInternalServerErrorHasOccurred(BaseException):
    pass


class InTestModeTheApplicationMustBeTurnedOffOrTheUserMustBeLoggedIn(BaseException):
    pass


class YouNeedToEnterTheCodeFromTheImageCaptcha(BaseException):
    pass


class AccessIsDenied(BaseException):
    pass


class RequestsMustBeMadeOverHTTPSBecauseTheUserHasEnabledASettingThatRequiresWorkOverASecureConnection(BaseException):
    pass


class UserValidationRequired(BaseException):
    pass


class ThePageHasBeenRemovedOrBlocked(BaseException):
    pass


class ThisActionIsProhibitedForNonStandaloneApplications(BaseException):
    pass


class ThisActionIsAllowedOnlyForStandaloneAndOpenAPIApplications(BaseException):
    pass


class TheMethodHasBeenDisabled(BaseException):
    pass


class UserConfirmationRequired(BaseException):
    pass


class TheCommunityAccessKeyIsInvalid(BaseException):
    pass


class TheApplicationAccessKeyIsInvalid(BaseException):
    pass


class QuantityLimitPerMethodCallReached(BaseException):
    pass


class ProfileIsPrivate(BaseException):
    pass


class OneOfTheRequiredParametersWasNotPassedOrIsInvalid(BaseException):
    pass


class InvalidApplicationAPIID(BaseException):
    pass


class InvalidUserID(BaseException):
    pass


class InvalidTimestamp(BaseException):
    pass


class AlbumAccessDenied(BaseException):
    pass


class AudioAccessDenied(BaseException):
    pass


class GroupAccessDenied(BaseException):
    pass


class AlbumFull(BaseException):
    pass


class ActionDeniedYouMustEnableVoiceTranslationsInTheAppSettings(BaseException):
    pass


class NoRightsToPerformTheseOperationsWithTheAdvertisingAccount(BaseException):
    pass


class AnErrorOccurredWhileWorkingWithTheAdvertisingAccount(BaseException):
    pass


class SpecifiedLinkIsIncorrectCantFindSource(BaseException):
    pass


class AccessToPostCommentsDenied(BaseException):
    pass


class AccessToStatusRepliesDenied(BaseException):
    pass


class HyperlinksAreForbidden(BaseException):
    pass


class TooManyReplies(BaseException):
    pass


class AccessToWallsPostDenied(BaseException):
    pass


class AccessToWallsCommentDenied(BaseException):
    pass


class TooManyAdsPosts(BaseException):
    pass


class DonutIsDisabled(BaseException):
    pass


class ContentBlocked(BaseException):
    pass


class AccessToAddingPostDenied(BaseException):
    pass


class AdvertisementPostWasRecentlyAdded(BaseException):
    pass


class TooManyRecipients(BaseException):
    pass
