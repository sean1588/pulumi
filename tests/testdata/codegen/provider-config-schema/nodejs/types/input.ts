// *** WARNING: this file was generated by test. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";

export namespace config {
    export interface SandwichArgs {
        bread?: pulumi.Input<string>;
        veggies?: pulumi.Input<pulumi.Input<string>[]>;
    }
}
